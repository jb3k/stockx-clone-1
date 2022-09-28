from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    # demo = User(
    #     first_name='Demo', last_name="User", email='demo@aa.io', password='password')
    # marnie = User(
    #     first_name='Jon', last_name="User",  email='marnie@aa.io', password='password')
    # bobbie = User(
    #     first_name='Ron', last_name="User",  email='bobbie@aa.io', password='password')

    # db.session.add(demo)
    # db.session.add(marnie)
    # db.session.add(bobbie)

    users = [
        {
            "first_name": "Demo",
            "last_name": "User",
            "email": "demouser@gmail.com",
            "password": "password"
        }, 
        {
            "first_name": "John",
            "last_name": "Demo",
            "email": "johndemo@gmail.com",
            "password": "password"
        }, 
        {
            "first_name": "Ron",
            "last_name": "Demo",
            "email": "rondemo@gmail.com",
            "password": "password"
        } 

    ]

    for user in users:

        new_user = User(
            first_name = user["first_name"],
            last_name = user["last_name"],
            email = user["email"],
            password = user["password"],
        )

        db.session.add(new_user)

    db.session.commit()
    print('Users were succesfully created')


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
