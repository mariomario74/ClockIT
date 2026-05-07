from gpiozero import Buzzer
import time

BUZZER_PIN = 17

# gpiozero automatically handles mock mode when not on real hardware
buzzer = Buzzer(BUZZER_PIN)

# Test buzzer: turn on for 1 second
print(f"Testing buzzer on pin {BUZZER_PIN}...")
buzzer.on()
time.sleep(1)
buzzer.off()

print("Buzzer test complete!")
buzzer.close()