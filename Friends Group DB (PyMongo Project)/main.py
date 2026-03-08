from pymongo import MongoClient

try:

    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)

    client.admin.command("ping")
    print("Connected successfully")

    # other application code

    # Creating a database DingDong
    # Creating a collection Members
    database = client["DingDong"]
    collection = database["Members"]

    #Adding information of members
    insert_action = input("Do you want to add new members? (y/n): ")

    document_count = collection.count_documents({})
    insert_count = 0
    if document_count > 0 :
        insert_count = document_count
    else :
        insert_count = 0

    while(insert_action == "y"):
        insert_count += 1
        #creating dictionary for each member
        memberInfo = {
            "_id" : insert_count,
            "name" : input("Enter name: "),
            "gender" : input("Enter gender: "),
            "age" : int(input("Enter age: ")),
            "height" : int(input("Enter height: ")),
            "nickname" : input("Enter nickname: ")
        }

        print("Inserting document...")
        member_id = collection.insert_one(memberInfo).inserted_id
        print("Document inserted!")
        print(f"New Member id is {member_id}")
        print("\n")
        # Accepting more inputs?
        insert_action = input("Do you want to add more members? (y/n): ")

    client.close()
    print("Connection closed")

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)

