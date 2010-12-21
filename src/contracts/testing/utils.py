from ..interface import ContractSyntaxError, describe_value
from ..main import parse_contract_string, check_contracts


def check_contracts_ok(contract, value):
    if isinstance(contract, str):
        contract = [contract]
        value = [value]
    check_contracts(contract, value)
            
def check_contracts_fail(contract, value, error):
    if isinstance(contract, str):
        contract = [contract]
        value = [value]
        
    try:
        context = check_contracts(contract, value)
        
        msg = 'I was expecting that the values would not not satisfy the contract.\n'
        
        for v in value:
            msg += '      value: %s\n' % describe_value(v) 
        
        for c in contract:
            cp = parse_contract_string(c)
            msg += '   contract: %r, parsed as %r (%s)\n' % (c, cp, cp)
               
        msg += '    context:  %r\n' % context

        raise Exception(msg)
    
    except error:
        pass

def check_syntax_fail(string):
    assert isinstance(string, str)
    
    try:
        parsed_contract = parse_contract_string(string)
        msg = 'I would not expect to parse %r.' % string
        msg += ' contract:         %s\n' % parsed_contract
        raise Exception(msg)
    
    except ContractSyntaxError:
        pass
    
