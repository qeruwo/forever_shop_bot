from aiogram.types import FSInputFile

#catalog

def catalog_list():
    list_catalog = []
        
    list_catalog.append(FSInputFile("photos/icons/cat.jpg", filename="cat_ass"))
    list_catalog.append(FSInputFile("photos/icons/fuck.jpg", filename="fuck"))
    list_catalog.append(FSInputFile("photos/icons/lion.jpg", filename="lion"))
    list_catalog.append(FSInputFile("photos/icons/los.jpg", filename="los"))
    return list_catalog