from database.database_ifc import DBIfc
from pymongo import MongoClient

class MongoDatabase(DBIfc):
    def __init__(self):
        self.uri = "mongodb+srv://cluster0.f7pfk.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
        self.client = MongoClient(self.uri,
                        tls=True,
                        tlsCertificateKeyFile='./database/X509-cert-443077859298030389.pem')
        self.db = self.client['rcp']
        self.collection = self.db['books']
    
    def store(self, book):
        '''
        The __dict__ contains a dict with every attribute of the object
        We store this dict directly into the database
        '''
        self.collection.insert_one(book.__dict__)
    
    def all_books(self):
        """
        Returns a list of all available books
        """
        return [book for book in self.collection.find({})]
