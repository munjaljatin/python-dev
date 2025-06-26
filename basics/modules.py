# import pyjokes
import pyttsx3

from pyjokes import get_joke as main

# joke = pyjokes.main()
# joke = main()
print(main())

engine = pyttsx3.init()
# engine.say("Hi Jatin! How are you?")
engine.say("This is the engine speaking to Jatin.")
engine.runAndWait()

# engine.say("Speaking")