import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self,email,password,_id=None):
        self.email=email
        self.password=password
    # gives us the html string of this unique identifier
    # generate a unique id
        self._id=uuid.uuid4().hex if _id is None else _id


    def __repr__(self):
        return "<User {}>".format(self.email)


    @staticmethod
    # not a speific user method, but the general methods thing user as a whole
    def is_login_valid(email,password):
        '''
        This method verifies that an email-password combo is valid or not
        Check that email exists, and that password associated to that email is correct
        :param email: The user'e email
        :param password: A sha512 hashed password not a plain text password
        :return:
        '''
        # check whether the user exists
        user_data=Database.find_one("users",{"email":email})
        if user_data is None:
            # Tell the user their email doesn't exists and they need to register
            raise UserErrors.UserNotExistsError("Your user doesn't exist.")
        if not Utils.check_hashed_password(password,user_data['password']):
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")

        return True