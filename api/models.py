"""Pydantic models definitions

Author: Aaron Kaplan
License: see LICENSE.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Union, List

import datetime


class Leak(BaseModel):
    id: Optional[int]
    ticket_id: Optional[int]
    summary: str
    reporter_name: Optional[str]
    source_name: Optional[str]
    breach_ts: Optional[datetime.datetime]
    source_publish_ts: Optional[datetime.datetime]


class LeakData(BaseModel):
    id: Optional[int]
    leak_id: int
    email: EmailStr
    password: str
    password_plain: Optional[str]
    password_hashed: Optional[str]
    hash_algo: Optional[str]
    ticket_id: Optional[str]
    email_verified: Optional[bool]
    password_verified_ok: Optional[bool]
    ip: Optional[str]
    domain: Optional[str]
    browser: Optional[str]
    malware_name: Optional[str]
    infected_machine: Optional[str]
    dg: Optional[str]


class AnswerMeta(BaseModel):
    version: str
    duration: float


class Answer(BaseModel):
    meta: Optional[AnswerMeta]
    data: Union[Dict,List]
    error: Optional[str]
