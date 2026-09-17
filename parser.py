import pyparsing as pp


class Parser():
    
    def __init__(self):
        pass
    
    def parse(self, query):
        
        
        
        title = pp.CaselessKeyword("Title")
        year = pp.CaselessKeyword("Year")
        rating = pp.CaselessKeyword("Rating")
        
        title_only_operators = pp.one_of("== !=").set_name("title comparison operator (== or !=)")
        operator = pp.one_of("== != < > <= >=").set_name("Comparison operator (== != < > <= >=)")
        
        movie_name = pp.QuotedString('"').set_name("movie name in quotes")
        
        get = pp.CaselessKeyword("Get")
        
        #get statement follows a title statement optionally
        optional_get_statement = pp.Optional(get + year | get + rating )
        
        #grammar 1
        title_statement = title + title_only_operators + movie_name + optional_get_statement
        
        #grammar 2
        num_value = pp.pyparsing_common.number.set_name("numeric value")
        year_statement = year + operator + num_value
        
        #grammar 3
        
        rating_statement = rating + operator + num_value
        
        
        #overall statement
        
        statement = title_statement ^ year_statement ^ rating_statement
        
        #connecting multiple statements with AND/OR
        connectors = pp.one_of("and or", caseless=True).set_name("connector (and/or)")
        expression = statement + pp.ZeroOrMore(connectors + statement)
        
        try:
            result = expression.parse_string(query, parse_all=True)
            success = True
            return success, result
        except pp.ParseBaseException as e:
            success = False
            return success, str(e)
    
parser = Parser()
    
print(parser.parse('Title == "The Shawshank Redemption" and Year > 2000 '))

