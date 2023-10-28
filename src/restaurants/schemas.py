from datetime import time, datetime
from typing import Literal, List, Optional
from uuid import UUID

from pydantic import BaseModel, HttpUrl


class WorkingHoursDTO(BaseModel):
	day: Literal[
		"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"
	]
	open: time
	close: time


class CreateRestaurantDTO(BaseModel):
	name: str
	description: str
	address: str
	phone: str
	website: HttpUrl
	working_hours: List[WorkingHoursDTO]


class CreateRestaurantResponse(BaseModel):
	id: UUID
	name: str
	description: str
	address: str
	phone: str
	website: HttpUrl
	working_hours: dict[str, list[dict[str, str]]]
	created_at: datetime
	updated_at: datetime
	deleted_at: Optional[datetime]