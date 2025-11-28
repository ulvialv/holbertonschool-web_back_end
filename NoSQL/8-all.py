#!/usr/bin/env python3
""" Lists all documents in a collection """

def list_all(mongo_collection):
    """
    Returns a list of all documents in a MongoDB collection.
    If no documents exist, returns an empty list.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
        list: A list of documents (dictionaries) in the collection.
    """
    # Use find() to get all documents and convert the cursor to a list
    return list(mongo_collection.find())
