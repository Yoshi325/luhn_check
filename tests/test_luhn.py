import sys
sys.path.append("..")
import luhn_check


class WhenPassingAValidAmericanExpressNumber():
    @classmethod
    def examples_of_american_express_card_numbers(cls):
        yield '378282246310005',  { 'luhn': True, 'chars': True, 'length': True }
        yield '343434343434343',  { 'luhn': True, 'chars': True, 'length': True }
        yield '370000000000002',  { 'luhn': True, 'chars': True, 'length': True }
        yield '340000000000009',  { 'luhn': True, 'chars': True, 'length': True }
        yield '371449635398431',  { 'luhn': True, 'chars': True, 'length': True }
        yield '378734493671000',  { 'luhn': True, 'chars': True, 'length': True }

    def because_we_validate_the_card_number(self, target, _):
        self.result = {
            'luhn': luhn_check.is_luhn_valid(target)
          , 'chars': luhn_check.is_card_chars_valid(target)
          , 'length': luhn_check.is_card_length_valid(target)
        }

    def the_luhn_check_should_return(self, _, expected):
        assert self.result['luhn'] == expected['luhn']
        assert self.result['chars'] == expected['chars']
        assert self.result['length'] == expected['length']

class WhenPassingAValidVisaNumber():
    @classmethod
    def examples_of_visa_card_numbers(cls):
        yield '4111111111111111',  { 'luhn': True, 'chars': True, 'length': True }
        yield '4007000000027',     { 'luhn': True, 'chars': True, 'length': True }
        yield '4222222222222',     { 'luhn': True, 'chars': True, 'length': True }
        yield '4012888888881881',  { 'luhn': True, 'chars': True, 'length': True }

    def because_we_validate_the_card_number(self, target, _):
        self.result = {
            'luhn': luhn_check.is_luhn_valid(target)
          , 'chars': luhn_check.is_card_chars_valid(target)
          , 'length': luhn_check.is_card_length_valid(target)
        }

    def the_luhn_check_should_return(self, _, expected):
        assert self.result['luhn'] == expected['luhn']
        assert self.result['chars'] == expected['chars']
        assert self.result['length'] == expected['length']

class WhenPassingAValidMasterCardNumber():
    @classmethod
    def examples_of_mastercard_card_numbers(cls):
        yield '5105105105105100', { 'luhn': True, 'chars': True, 'length': True }
        yield '5111111111111118', { 'luhn': True, 'chars': True, 'length': True }
        yield '5454545454545454', { 'luhn': True, 'chars': True, 'length': True }
        yield '5500000000000004', { 'luhn': True, 'chars': True, 'length': True }
        yield '5555555555554444', { 'luhn': True, 'chars': True, 'length': True }

    def because_we_validate_the_card_number(self, target, _):
        self.result = {
            'luhn': luhn_check.is_luhn_valid(target)
          , 'chars': luhn_check.is_card_chars_valid(target)
          , 'length': luhn_check.is_card_length_valid(target)
        }

    def the_luhn_check_should_return(self, _, expected):
        assert self.result['luhn'] == expected['luhn']
        assert self.result['chars'] == expected['chars']
        assert self.result['length'] == expected['length']

class WhenPassingAValidDiscoverCardNumber():
    @classmethod
    def examples_of_discover_card_numbers(cls):
        yield '6011111111111117', { 'luhn': True, 'chars': True, 'length': True }
        yield '6011000000000004', { 'luhn': True, 'chars': True, 'length': True }
        yield '6011000990139424', { 'luhn': True, 'chars': True, 'length': True }
        yield '6011601160116611', { 'luhn': True, 'chars': True, 'length': True }
        yield '6111111111111116', { 'luhn': True, 'chars': True, 'length': True }

    def because_we_validate_the_card_number(self, target, _):
        self.result = {
            'luhn': luhn_check.is_luhn_valid(target)
          , 'chars': luhn_check.is_card_chars_valid(target)
          , 'length': luhn_check.is_card_length_valid(target)
        }

    def the_luhn_check_should_return(self, _, expected):
        assert self.result['luhn'] == expected['luhn']
        assert self.result['chars'] == expected['chars']
        assert self.result['length'] == expected['length']

if __name__ == '__main__':
    import contexts
    contexts.main()
