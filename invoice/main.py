from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base, InvoiceCompare
from pydantic import BaseModel
from typing import  Optional
from datetime import datetime

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

class InvoiceSchema(BaseModel):
    invoice_compare_id: str
    account_number: str
    end_date: Optional[datetime] = None
    external_reference: Optional[str] = None
    account_name: str
    invoice_id: str
    invoice_number: str
    invoice_date: Optional[datetime] = None
    source_lines_json: Optional[dict] = None
    target_lines_json: Optional[dict] = None
    compare_lines_json: Optional[dict] = None
    status_cd: Optional[str] = None
    created_by: str
    creation_dttm: Optional[datetime] = None
    modified_by: Optional[str] = None
    modified_dttm: Optional[datetime] = None
    version: Optional[float] = None
    cycle_run_id: Optional[str] = None

    class Config:
        from_attributes  = True
        json_encoders = {datetime: lambda v: v.isoformat()} 

@app.post("/invoices/", response_model=InvoiceSchema)
def create_invoice(invoice: InvoiceSchema, db: Session = Depends(get_db)):
    db_invoice = InvoiceCompare(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

@app.get("/invoices/{invoice_compare_id}", response_model=InvoiceSchema)
def get_invoice(invoice_compare_id: str, db: Session = Depends(get_db)):
    invoice = db.query(InvoiceCompare).filter(InvoiceCompare.invoice_compare_id == invoice_compare_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@app.put("/invoices/{invoice_compare_id}", response_model=InvoiceSchema)
def update_invoice(invoice_compare_id: str, invoice: InvoiceSchema, db: Session = Depends(get_db)):
    db_invoice = db.query(InvoiceCompare).filter(InvoiceCompare.invoice_compare_id == invoice_compare_id).first()
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    for key, value in invoice.dict(exclude_unset=True).items():
        setattr(db_invoice, key, value)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

@app.delete("/invoices/{invoice_compare_id}")
def delete_invoice(invoice_compare_id: str, db: Session = Depends(get_db)):
    db_invoice = db.query(InvoiceCompare).filter(InvoiceCompare.invoice_compare_id == invoice_compare_id).first()
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    db.delete(db_invoice)
    db.commit()
    return {"message": "Invoice deleted successfully"}