from backend.app.db.repositories.base import BaseRepository
from backend.app.models.cleanings import CleaningCreate, CleaningInDB

CREATE_CLEANING_QUERY = """
    INSERT INTO cleanings (name, description, price, cleaning_type)
    VALUES (:name, :description, :price, :cleaning_type)
    RETURNING id, name, description, price, cleaning_type;
"""

class CleaningRepositry(BaseRepository):
    """All database actions associated with Cleaning resource

    Args:
        BaseRepository (_type_): _description_
    """

    async def create_cleaning(self, *, new_cleaning: CleaningCreate) -> CleaningInDB:
        query_values = new_cleaning.dict()
        cleaning = await self.db.fetch_one(query=CREATE_CLEANING_QUERY, values=query_values)

        return CleaningInDB(**cleaning)
    