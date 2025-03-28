from sqlalchemy import Column, String, TIMESTAMP, Numeric, JSON
from database import Base

class InvoiceCompare(Base):
    __tablename__ = "invoice_compare"
    
    invoice_compare_id = Column(String(50), primary_key=True, index=True)
    account_number = Column(String(50), nullable=False)
    end_date = Column(TIMESTAMP, nullable=True)
    external_reference = Column(String(254), nullable=True)
    account_name = Column(String(50), nullable=False)
    invoice_id = Column(String(50), nullable=False)
    invoice_number = Column(String(50), nullable=False)
    invoice_date = Column(TIMESTAMP, nullable=True)
    source_lines_json = Column(JSON, nullable=True)
    target_lines_json = Column(JSON, nullable=True)
    compare_lines_json = Column(JSON, nullable=True)
    status_cd = Column(String(3), nullable=True)
    created_by = Column(String(50), nullable=False)
    creation_dttm = Column(TIMESTAMP, nullable=True)
    modified_by = Column(String(50), nullable=True)
    modified_dttm = Column(TIMESTAMP, nullable=True)
    version = Column(Numeric(5), nullable=True)
    cycle_run_id = Column(String(30), nullable=True)
