# OPTION 1
import winsound

# Play a beep sound when finished
winsound.Beep(1000, 1000)  # frequency, duration


# OPTION 2
import winsound

# Play Windows default sound
winsound.MessageBeep()


#OPTION 3
print("DONE ✅")

import winsound
winsound.Beep(1500, 1500)


#OPTION 4
## pip install plyer
from plyer import notification

notification.notify(
    title="Job Mapping",
    message="Processing finished ✅",
    timeout=5
)

#OPTION 5
print("🚀 Job mapping started...")

# your code here

print("✅ Job mapping completed!")


# OPTION 6 SMART

for i, (_, row) in enumerate(df.iterrows()):
    if i % 50 == 0:
        print(f"Processed {i} rows")


#OPTION 7 COMBO SAMPLE
print("🚀 Job mapping started...")

df = df.apply(map_row, axis=1)

print("✅ Job mapping completed!")

import winsound
winsound.Beep(1500, 1000)


#OPTION 8 COMBO SAMPLE
import winsound
print("✅ DONE")
winsound.Beep(500, 200);winsound.Beep(1500, 200);winsound.Beep(1000, 200)  # frequency, duration
