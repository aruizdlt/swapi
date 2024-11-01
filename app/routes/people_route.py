from typing import List

from fastapi import APIRouter, HTTPException

from app.config.logging import logger
from app.schemas.person_schema import PersonSchema
from app.services.people_service import PeopleService

router = APIRouter()

@router.get("/people", response_model=List[PersonSchema])
def get_people():
    try:
        logger.info("Fetching people from SWAPI")
        people = PeopleService.get_people()
        logger.info("Successfully fetched people")
        return people
    except Exception as e:
        logger.warning(f"Error fetching people: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/people/names-sorted", response_model=List[str])
def get_people_names_sorted():
    try:
        logger.info("Fetching people names sorted from SWAPI")
        names = PeopleService.get_people_names_sorted()
        logger.info("Successfully fetched people")
        return names
    except Exception as e:
        logger.warning(f"Error fetching people: {e}")
        raise HTTPException(status_code=500, detail=str(e))