from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime
from src.database import Base


class Admin(Base):
    __tablename__ = "com_admin"

    admin_idx: int | Column = Column(Integer, name="admin_idx", nullable=False, autoincrement=True, primary_key=True)
    email: str | Column = Column(String(255), name="email", nullable=False)
    password: str | Column = Column(String(100), name="password", nullable=False)
    admin_nm: str | Column = Column(String(100), name="admin_nm", nullable=False)
    role_cd: str | Column = Column(String(30), name="role_cd", nullable=False, default="NORMAL")
    use_yn: str | Column = Column(String(1), name="use_yn", nullable=False, default="Y")
    created_at: datetime | Column = Column(DateTime, name="created_at", nullable=False,
                                           default=datetime.now(UTC))
    created_by: int | Column = Column(Integer, name="created_by", nullable=False)
    updated_at: datetime | Column = Column(DateTime, name="updated_at", nullable=True)
    updated_by: int | Column = Column(Integer, name="updated_by", nullable=True)


class MasterCode(Base):
    __tablename__ = "com_mst_code"
    mst_cd:str | Column = Column(String(30), name="mst_cd", nullable=False, primary_key=True)
    mst_cd_nm: str | Column = Column(String(50), name="mst_cd_nm", nullable=False)
    mst_cd_desc: str | Column = Column(String(100), name="mst_cd_desc", nullable=True)
    use_yn: str | Column = Column(String(1), name="use_yn", nullable=False, default="Y")
    created_at: datetime | Column = Column(DateTime, name="created_at", nullable=False,
                                           default=datetime.now(UTC))
    created_by: int | Column = Column(Integer, name="created_by", nullable=False)
    updated_at: datetime | Column = Column(DateTime, name="updated_at", nullable=True)
    updated_by: int | Column = Column(Integer, name="updated_by", nullable=True)


class Code(Base):
    __tablename__ = "com_sub_code"
    mst_cd:str | Column = Column(String(30), name="mst_cd", nullable=False, primary_key=True)
    sub_cd: str | Column = Column(String(30), name="sub_cd", nullable=False, primary_key=True)
    code_nm: str | Column = Column(String(50), name="code_nm", nullable=False)
    code_desc: str | Column = Column(String(100), name="code_desc", nullable=True)
    order_no: str | Column = Column(Integer, name="order_no", nullable=False, default=1)
    use_yn: str | Column = Column(String(1), name="use_yn", nullable=False, default="Y")
    created_at: datetime | Column = Column(DateTime, name="created_at", nullable=False,
                                           default=datetime.now(UTC))
    created_by: int | Column = Column(Integer, name="created_by", nullable=False)
    updated_at: datetime | Column = Column(DateTime, name="updated_at", nullable=True)
    updated_by: int | Column = Column(Integer, name="updated_by", nullable=True)
