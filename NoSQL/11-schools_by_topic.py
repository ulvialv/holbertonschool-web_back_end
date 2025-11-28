#!/usr/bin/env python3
""" Returns a list of schools having a specific topic """

def schools_by_topic(mongo_collection, topic):
    """
    Returns all documents in a MongoDB collection that have a specific topic in their 'topics' field.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of documents (schools) that have the specified topic.
    """
    # Query for documents where 'topics' array contains the given topic
    return list(mongo_collection.find({ "topics": topic }))
