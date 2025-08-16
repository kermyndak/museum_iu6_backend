from sqlalchemy import (
    Column, Integer, BigInteger, String, Text, Boolean, DateTime, ForeignKey, JSON
)
from sqlalchemy.orm import relationship
from .database import Base


class ActiveStorageBlob(Base):
    __tablename__ = "active_storage_blobs"

    id = Column(BigInteger, primary_key=True)
    key = Column(String, unique=True, nullable=False)
    filename = Column(String, nullable=False)
    content_type = Column(String)
    metadata = Column(Text)
    service_name = Column(String, nullable=False)
    byte_size = Column(BigInteger, nullable=False)
    checksum = Column(String)
    chapter = Column(String)
    success = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False)

    attachments = relationship("ActiveStorageAttachment", back_populates="blob", cascade="all, delete-orphan")
    variants = relationship("ActiveStorageVariantRecord", back_populates="blob", cascade="all, delete-orphan")


class ActiveStorageAttachment(Base):
    __tablename__ = "active_storage_attachments"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    record_type = Column(String, nullable=False)
    record_id = Column(BigInteger, nullable=False)
    blob_id = Column(BigInteger, ForeignKey("active_storage_blobs.id"), nullable=False)
    created_at = Column(DateTime, nullable=False)

    blob = relationship("ActiveStorageBlob", back_populates="attachments")


class ActiveStorageVariantRecord(Base):
    __tablename__ = "active_storage_variant_records"

    id = Column(BigInteger, primary_key=True)
    blob_id = Column(BigInteger, ForeignKey("active_storage_blobs.id"), nullable=False)
    variation_digest = Column(String, nullable=False)

    blob = relationship("ActiveStorageBlob", back_populates="variants")


class ARInternalMetadata(Base):
    __tablename__ = "ar_internal_metadata"

    key = Column(String, primary_key=True)
    value = Column(String)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class Request(Base):
    __tablename__ = "requests"

    id = Column(BigInteger, primary_key=True)
    message = Column(Text)
    read = Column(Boolean, default=False)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="requests")


class SchemaMigration(Base):
    __tablename__ = "schema_migrations"

    version = Column(String, primary_key=True)


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(BigInteger, primary_key=True)
    fio = Column(Text)
    job_title = Column(Text)
    additional_information = Column(JSON, default="")
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    email = Column(String, nullable=False, default="", unique=True)
    encrypted_password = Column(String, nullable=False, default="")
    reset_password_token = Column(String, unique=True)
    reset_password_sent_at = Column(DateTime)
    remember_created_at = Column(DateTime)
    confirmation_token = Column(String)
    confirmed_at = Column(DateTime)
    confirmation_sent_at = Column(DateTime)
    unconfirmed_email = Column(String)
    name = Column(String)
    surname = Column(String)
    middle_name = Column(String)
    year = Column(Integer)
    role = Column(String, default="user")
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    requests = relationship("Request", back_populates="user", cascade="all, delete-orphan")
