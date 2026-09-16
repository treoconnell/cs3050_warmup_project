import pyparsing as pp


class Parser():
    
    def __init__(self):
        pass
    
    def parse(self, query):
        
        
        #grammar 1
        title = pp.Keyword("Title")
        
        operator = pp.one_of("== !=")
        
        value = pp.QuotedString('"')
        
        connector = pp.one_of("OR AND")
        
        
        title_statement = title + operator + value
        
        return title_statement.parse_string(query)
    
parser = Parser()
    
print(parser.parse('Title == "Airbuds 2" '))