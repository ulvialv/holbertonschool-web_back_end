#!/usr/bin/env python3
""" Updates all topics of school documents based on the school name """

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all documents in a MongoDB collection where 'name' matches.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list of str): List of topics to set for the school.
    """
    mongo_collection.update_many(
        { "name": name },          # filter: select all matching documents
        { "$set": { "topics": topics } }  # update: set the 'topics' field
    )
