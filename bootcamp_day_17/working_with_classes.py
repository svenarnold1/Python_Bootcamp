# this files a way to work with classes

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User('001', 'Sven')
user_2 = User('002', 'Arnold')

# user 1 is following user 2
user_1.follow(user_2)

print(f" user 1 followers: {user_1.follower}, user 1 following: {user_1.following}")
print(f" user 2 followers: {user_2.follower}, user 2 following: {user_2.following}")
