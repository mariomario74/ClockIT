import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Initialize the scanner
reader = SimpleMFRC522()

try:
    print("Waiting for RFID tag...")
    # This pauses the script until a card is tapped
    id, text = reader.read()
    
    print(f"Tag ID: {id}")
    print(f"Text: {text}")

except KeyboardInterrupt:
    print("\nScanner stopped manually.")

finally:
    # This safely releases the SPI pins back to the system
    GPIO.cleanup()
    print("Pins cleaned up.")