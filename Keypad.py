import RPi.GPIO as GPIO
import time

class keypad():

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.matrix=[['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['#','0','*']]
        self.row_pins=[18,23,24,25]
        self.col_pins=[17,27,22]
        for j in range(3):
            GPIO.setup(self.col_pins[j], GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        for i in range(4):
            GPIO.setup(self.row_pins[i], GPIO.OUT)

    def do_polling(self):
        #Determine currently pressed key
        pressedButton=None
        for i in range(4):
            GPIO.output(self.row_pins[i],GPIO.HIGH)
            for j in range(3):
                time.sleep(0.2)
                if GPIO.input(self.col_pins[j])==GPIO.HIGH:
                    pressedButton=(i,j)
                    break
            GPIO.output(self.row_pins[i],GPIO.LOW)
            if pressedButton!=None:
                break
        if pressedButton!=-1:
            return self.matrix[pressedButton[0]][pressedButton[1]]
        else:
            return None


    def get_next_signal(self):
        signal = None
        while signal == None:
            signal = self.do_polling()
        return signal


if __name__=="__main__":
    kp=keypad()
    kp.setup()
    string=""
    while string!="5468":
        poll=kp.do_polling()
        if poll!="":
            print(poll)
            string+=poll
    print(string)