import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

BUZZER_PIN = 17
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Make sure it starts completely quiet
GPIO.output(BUZZER_PIN, GPIO.LOW)

reader = SimpleMFRC522()

try:
    print("Waiting for RFID tag...")
    # This pauses the script until a card is tapped
    id, text = reader.read()
    
    print(f"Tag ID: {id}")
    print(f"Text: {text}")

    for i in range(3):
        GPIO.output(BUZZER_PIN, GPIO.HIGH) # Sound ON
        time.sleep(0.1)
        GPIO.output(BUZZER_PIN, GPIO.LOW)  # Sound OFF
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nScanner stopped manually.")

finally:
    # This safely releases the SPI pins back to the system
    GPIO.cleanup()
    print("Pins cleaned up.")