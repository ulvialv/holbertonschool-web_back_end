#!/usr/bin/env python3
""" Updates all topics of a school document based on the school name """

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a document in a MongoDB collection where 'name' matches.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list of str): List of topics to set for the school.
    """
    mongo_collection.update_one(
        { "name": name },        # filter: select the document to update
        { "$set": { "topics": topics } }  # update: set the 'topics' field
    )
