from models import SessionLocal, User, Address

# Start a session (think: open a connection)
session = SessionLocal()
try:
    # --- Create (INSERT) ---
    address = Address(street="123 Main St", number=1, county="Galway", country="Ireland", eircode="H91X77E")
    session.add(address)
    session.flush()  # Writes address, gets address.id, but does NOT commit

    user = User(name="Paul", email="paul@example.com", age=21, address_id=address.id)
    session.add(user)

    session.commit()  # Both address and user committed together!
    session.refresh(user)
    session.refresh(address)
    print(f"Added user: {user.name} with address: {address.street}")

    # --- Read (SELECT) ---
    users = session.query(User).all()
    for u in users:
        print(f"User: {u.name}, Email: {u.email}, Address: {u.address.street}")

    # --- Delete (DELETE) ---
    session.delete(user)
    session.commit()
    print("Deleted user:", user.name)

except Exception as e:
    session.rollback()
    print("Transaction failed:", e)
finally:
    session.close()