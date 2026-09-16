import pyparsing as pp


class Parser():
    
    def __init__(self):
        pass
    
    def parse(self, query):
        
        
        
        title = pp.Keyword("Title")
        year = pp.Keyword("Year")
        rating = pp.Keyword("Rating")
        
        title_only_operators = pp.one_of("== !=")
        operator = pp.one_of("== != < > <= >=")
        
        value = pp.QuotedString('"')
        
        get = pp.Keyword("Get")
        
        #get statement follows a title statement optionally
        optional_get_statement = pp.Optional(get + year | get + rating )
        
        #grammar 1
        title_statement = title + title_only_operators + value + optional_get_statement
        
        #grammar 2
        num_value = pp.pyparsing_common.number
        year_statement = year + operator + num_value
        
        #grammar 3
        
        rating_statement = rating + operator + num_value
        
        
        #overall statement
        
        statement = title_statement ^ year_statement ^ rating_statement
        
        #connecting multiple statements with AND/OR
        connectors = pp.one_of("and or")
        expression = statement + pp.ZeroOrMore(connectors + statement)
        
        return expression.parse_string(query)
    
parser = Parser()
    
print(parser.parse('Title  == "The Shawshank Redemption" and Year > 2000'))