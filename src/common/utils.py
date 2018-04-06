from passlib.hash import pbkdf2_sha512

class Utils(object):

    @staticmethod
    def hash_password(password):
        '''
        Hashes a password using pbdff2_sha512
        :param password: The sha512 password from the login/register form
        :return: A sha512->pbkdf2_sha512 encrypted password
        double encrypting
        '''
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def checked_hashed_password(password,hashed_password):
        """
        Checks that the password the user sent matches that of database.


        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True if passwords match, False otherwise
        """

        return pbkdf2_sha512.verify(password,hashed_password)

