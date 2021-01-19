import unittest
from decoding_contour_next_link \
    import PumpStatusResponseMessage

from datetime import datetime, time

from unittest_data_provider import data_provider

class TestPumpStatusDecode(unittest.TestCase):

    data_PumpStatusResponseMessage_TrendArrowsProvider = lambda: (
        (1, '02013C1000000000000000000000000000004A38278D901C48000200001676000000000000000000EB5A640015EB541900000000000000000000000000000000000000000000000000000000000000000000000000000000000008D6000008D6', 
            None, None),

        (2, '02013C5000000000000000000000000000009C40278B41A13500010000138800000000000000000128E032001DB38419000000A028006A86755455A115F6670000100000E12AFE0D00000000000000000000000000000000000008C7000008C7',
            '3 arrows down', -3),
        (3, '02013C5000000000000000000000000000003E80278EDD245700020000109A000000000000000000BF684B00113640190000001B58007A8678FA64A115F6670001100001E012FE8C00000000000000000000000000000000000008DD000008DD', 
            '3 arrows down', -3),

        (4, '02013C5000000000000000000000000000002328278BDD283A00010000109A0000000000000000003A9819001C2ED819000000232800E28675E6D5A115F6670020100002D529FF350000FF00688675E6F9A115F667000000000008C8000008C8', 
            '2 arrows down', -2),
        (5, '02013C5000000000000000000000000000003E80278EDD245700020000109A000000000000000000BC7A4B0011392E190000001F4000A48678F80CA115F6670021100001EA12FF2500000000000000000000000000000000000008DD000008DD', 
            '2 arrows down', -2),

        (6, '02013C5000000000000000000000000000002328278BDD283A00010000109A0000000000000000004B3219001C1E3E19000000177000DC8675F4E5A115F66700401000029929FF9B00000000688675E6F9A115F667000000000008C8000008C8', 
            '1 arrow down', -1),
        (7, '02013C600000000000000000000000000000BF68278EB947560052000011940000000032006B00009F2E4B001194FA190000005DC0002B8678D73BA115F6670A411000027613FF6600000000000000000000000000000000000008DD000008DD', 
            '1 arrow down', -1),

        (8, '02013C5000000000000000000000000000009C40278B41A13500010000177000000000000000000131AA32001DAABA190000004E2000448675600DA115F6670860100000AF2AFFC400000000000000000000000000000000000008C7000008C7', 
            'No arrows', 0),
        (9, '02013C5000000000000000000000000000000FA0278E654D5300020000109A00000000000000000031CE4B0012EAC61900000007D000C286788080A115F66700611000028A15000200000003668678714DA115F667000000000008DD000008DD', 
            'No arrows', 0),

        (10, '02013C52000023280000000000003B0000002328278BDD283A000100000CB2000000000000000000C63E19001B800A19000000232800D086765882A115F6670580100002B729007500000000000000000000000000000000000008C9000008C9', 
            '1 arrow up', 1),
        (11, '02013C500000000000000000000000000000BF68278EB94756000200000DAC000000000000000000A4104B0011901819000000177000968678E54BA115F66700811000023A11009100000000000000000000000000000000000008DD000008DD', 
            '1 arrow up', 1),

        (12, '02013C5000000000000000000000000000001770278D17554500020000109A00000000000000000042686400175B7E190000000BB800EE86773D0AA115F66700A01400025D2700F500000000000000000000000000000000000008D4000008D4', 
            '2 arrows up', 2),
        (13, '02013C5000000000000000000000000000002EE0278F2EF7590002000017700000000000000000012BCE4B0010589219000000271000A3867940B6A115F66700A11000028A1100DA00000000000000000000000000000000000008DF000008DF', 
            '2 arrows up', 2),

        (14, '02013C5000000000000000000000000000004A38278D901C4800020000128E000000000000000000CF0864001607A6190000002AF8005E8677B369A115F66700C0100001AE26012F00000000000000000000000000000000000008D6000008D6', 
            '3 arrows up', 3),
        (15, '02013C5000000000000000000000000000002EE0278F46355B000200001C5200000000000000000155CC4B000FDC8C190000003E8000CD86795826A115F66705C1100000BE11014600000000000000000000000000000000000008DF000008DF', 
            '3 arrows up', 3),

        (16, '02013C5000000000000000000000000000001388278BAD133900010000109A00000000000000000037AA32001C54EE19000000000003028675E47DA115F66700E01400000029000000000003078675E103A115F667000000000008C8000008C8', 
            'Unknown trend', None),
        (17, '02013C5000000000000000000000000000004268278F0C015800020000186A000000000000000000FDE84B0010B5581900000023280302867925C0A115F66700E11400000011000000000000000000000000000000000000000008DE000008DE', 
            'Unknown trend', None),
    )

    @data_provider(data_PumpStatusResponseMessage_TrendArrowsProvider)
    def test_PumpStatusResponseMessage_TrendArrows(self, _ , raw, exp_arrows, exp_arrows_value):
        testobj = PumpStatusResponseMessage()
        testobj.responsePayload = bytearray.fromhex(raw)

        self.assertEquals(testobj.trendArrow, exp_arrows)
        self.assertEquals(testobj.trendArrowValue, exp_arrows_value)

if __name__ == '__main__':
    unittest.main()