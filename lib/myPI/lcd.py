from time import sleep

import smbus

class LCD1620:

    # Define some device parameters
    I2C_ADDR  = 0x3f # I2C device address #アドレスが違う場合もあるかもしれない
    LCD_WIDTH = 16   # Maximum characters per line
    
    # Define some device constants
    LCD_CHR = 1 # Mode - Sending data
    LCD_CMD = 0 # Mode - Sending command
    
    LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
    LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
    
    LCD_BACKLIGHT  = 0x08  # On
    #__LCD_BACKLIGHT = 0x00  # Off
    
    ENABLE = 0b00000100 # Enable bit
    
    # Timing constants
    E_PULSE = 0.0005
    E_DELAY = 0.0005


    KANA_CODE = {
        "　" : "\xA0",
        "。" : "\xA1",
        "「" : "\xA2",
        "」" : "\xA3",
        "、" : "\xA4",
        "・" : "\xA5",
        "ヲ" : "\xA6",
        "ァ" : "\xA7",
        "ィ" : "\xA8",
        "ゥ" : "\xA9",
        "ェ" : "\xAA",
        "ォ" : "\xAB",
        "ャ" : "\xAC",
        "ュ" : "\xAD",
        "ョ" : "\xAE",
        "ッ" : "\xAF",
        "ー" : "\xB0",
        "ア" : "\xB1",
        "イ" : "\xB2",
        "ウ" : "\xB3",
        "エ" : "\xB4",
        "オ" : "\xB5",
        "カ" : "\xB6",
        "キ" : "\xB7",
        "ク" : "\xB8",
        "ケ" : "\xB9",
        "コ" : "\xBA",
        "サ" : "\xBB",
        "シ" : "\xBC",
        "ス" : "\xBD",
        "セ" : "\xBE",
        "ソ" : "\xBF",
        "タ" : "\xC0",
        "チ" : "\xC1",
        "ツ" : "\xC2",
        "テ" : "\xC3",
        "ト" : "\xC4",
        "ナ" : "\xC5",
        "ニ" : "\xC6",
        "ヌ" : "\xC7",
        "ネ" : "\xC8",
        "ノ" : "\xC9",
        "ハ" : "\xCA",
        "ヒ" : "\xCB",
        "フ" : "\xCC",
        "ヘ" : "\xCD",
        "ホ" : "\xCE",
        "マ" : "\xCF",
        "ミ" : "\xD0",
        "ム" : "\xD1",
        "メ" : "\xD2",
        "モ" : "\xD3",
        "ヤ" : "\xD4",
        "ユ" : "\xD5",
        "ヨ" : "\xD6",
        "ラ" : "\xD7",
        "リ" : "\xD8",
        "ル" : "\xD9",
        "レ" : "\xDA",
        "ロ" : "\xDB",
        "ワ" : "\xDC",
        "ン" : "\xDD",
        "”" : "\xDE",
        "゜" : "\xDF"
    }

    def __init__(self):

        #Open I2C interface
        #__bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
        self.__bus = smbus.SMBus(1) # Rev 2 Pi uses 1

        self.__lcd_init()

    def __lcd_init(self):
        # Initialise display
        self.__lcd_byte(0x33,self.LCD_CMD) # 110011 Initialise
        self.__lcd_byte(0x32,self.LCD_CMD) # 110010 Initialise
        self.__lcd_byte(0x06,self.LCD_CMD) # 000110 Cursor move direction
        self.__lcd_byte(0x0C,self.LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
        self.__lcd_byte(0x28,self.LCD_CMD) # 101000 Data length, number of lines, font size
        self.__lcd_byte(0x01,self.LCD_CMD) # 000001 Clear display
        sleep(self.E_DELAY) 
      

    def __lcd_byte(self, bits, mode):
        # Send byte to data pins
        # bits = the data
        # mode = 1 for data
        #        0 for command
        
        bits_high = mode | (bits & 0xF0) | self.LCD_BACKLIGHT
        bits_low = mode | ((bits<<4) & 0xF0) | self.LCD_BACKLIGHT
        
        # High bits
        self.__bus.write_byte(self.I2C_ADDR, bits_high)
        self.__lcd_toggle_enable(bits_high)
        
        # Low bits
        self.__bus.write_byte(self.I2C_ADDR, bits_low)
        self.__lcd_toggle_enable(bits_low)
 
    def __lcd_toggle_enable(self, bits):
        # Toggle enable
        sleep(self.E_DELAY)
        self.__bus.write_byte(self.I2C_ADDR, (bits | self.ENABLE))
        sleep(self.E_PULSE)
        self.__bus.write_byte(self.I2C_ADDR,(bits & ~self.ENABLE))
        sleep(self.E_DELAY)
        
    def __lcd_string(self,message,line):
        # Send string to display
        message = message.ljust(self.LCD_WIDTH," ")
        self.__lcd_byte(line, self.LCD_CMD)
        for i in range(self.LCD_WIDTH):
            self.__lcd_byte(ord(message[i]),self.LCD_CHR)


    def clear(self):
        self.__lcd_init()
        sleep(self.E_DELAY)

    def kana_to_code(self,str):
        code = ""
        for c in str:
            code = code + self.KANA_CODE[c]
        return code

    def printLine1(self,line1):
        self.__lcd_string( line1 , self.LCD_LINE_1 )
        sleep(self.E_DELAY)
    
    def printLine2(self,line2):
        self.__lcd_string( line2 , self.LCD_LINE_2 )
        sleep(self.E_DELAY)
    

    def print(self,line1,line2):     
        self.__lcd_string( line1 , self.LCD_LINE_1 )
        self.__lcd_string( line2 , self.LCD_LINE_2 )
        sleep(self.E_DELAY)                     

if __name__ == '__main__':

    lcd = LCD1620()
    
    lcd.print("Hello","world")
    sleep(3)

    lcd.printLine1(lcd.kana_to_code("ハロー　ワールト”"))
    lcd.printLine2(lcd.kana_to_code("ハ”イハ”イ。サヨウナラ。"))
    sleep(3)

    lcd.clear()
    
