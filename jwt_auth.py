import jwt
from datetime import datetime, timezone
from typing import Dict, Optional

SECRET_KEY = "i-am-irfan-and-i-am-a-developer!"

def generate_jwt(user_id: str) -> str:

    expiration_time = datetime.now(timezone.utc) + datetime.timedelta(minutes=5)
    
    payload = {
        "sub": user_id,
        "role": "user",
        "exp": expiration_time  # Expiration claim
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    return token



def validate_jwt(token: str) -> tuple[bool, Optional[Dict]]:
    try:
        decoded_token = jwt.decode(
            token, 
            SECRET_KEY, 
            algorithms=["HS256"],
            options={"verify_exp": True}  
        )
        
        return True, decoded_token
    
    except jwt.ExpiredSignatureError:
        print("Token Invalid: Token has expired")
        return False, None
    
    except jwt.InvalidSignatureError:
        print("Token Invalid: Invalid signature")
        return False, None
    
    except jwt.InvalidTokenError as e:
        print(f"Token Invalid: {str(e)}")
        return False, None



def main():
    
    print("=" * 50)
    print("JWT Authentication System")
    print("=" * 50)
    
    while True:
        print("\nSelect an option:")
        print("1. Generate JWT Token")
        print("2. Validate JWT Token")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == "1":
            user_id = input("Enter user ID: ").strip()
            if not user_id:
                print("Error: User ID cannot be empty!")
                continue
            
            print(f"\nGenerating JWT for user: {user_id}")
            token = generate_jwt(user_id)
            print(f"\nGenerated Token:\n{token}\n")
            
        elif choice == "2":
            token = input("Enter JWT token to validate: ").strip()
            if not token:
                print("Error: Token cannot be empty!")
                continue
            
            print("\nValidating token...")
            is_valid, claims = validate_jwt(token)
            
            if is_valid:
                print("\nToken Valid")
                print(f"Claims: {claims}")
            else:
                print("\nToken Invalid")
                
        elif choice == "3":
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
