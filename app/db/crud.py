#TO-DO: подумать над condition, легко ли его реализовывать будет + сделать select-one, select-all + доделать update
from typing import Any, Type, TypeVar

from sqlalchemy import Result, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .database import Base

Model = TypeVar("Model", Base)

async def insert_obj(session: AsyncSession, model_obj: Model) -> bool:
    try:
        session.add(model_obj)
        await session.flush()
        # Промежуточные логи
        await session.commit()
    except: 
        return False
    
    return True

async def get_elem_by_value_field(session: AsyncSession, model: Type[Base], condition) -> Result:
    result = await session.execute(select(model).where(condition))
        
    return result

# async def get_elem_and_update(session: AsyncSession, model: Base, sfield: str, svalue: Any) -> Result:
#     result = await session.execute(select(model).where(getattr(model, field)) == value)
        
#     return result

async def delete_elem_by_value_field(session: AsyncSession, model: Type[Base], condition) -> Result:
    result = await session.execute(delete(model).where(condition))
        
    return result
