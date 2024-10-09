from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client.assignment_portal

class UserModel:
    @staticmethod
    def insert_user(data):
        users = db.users
        users.insert_one(data)

    @staticmethod
    def find_user_by_email(email):
        return db.users.find_one({"email": email})

    @staticmethod
    def insert_assignment(data):
        assignments = db.assignments
        assignments.insert_one(data)

class AdminModel:
    @staticmethod
    def insert_admin(data):
        admins = db.admins
        admins.insert_one(data)

    @staticmethod
    def find_admin_by_email(email):
        return db.admins.find_one({"email": email})

    @staticmethod
    def get_assignments_for_admin(admin_email):
        return list(db.assignments.find({"admin": admin_email}))

    @staticmethod
    def update_assignment_status(assignment_id, status):
        db.assignments.update_one(
            {"_id": ObjectId(assignment_id)},
            {"$set": {"status": status}}
        )

    @staticmethod
    def get_all_admins():
        admins = db.admins.find({}, {"_id": 0, "email": 1})
        return list(admins)
