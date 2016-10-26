
sol_func = """
function {func_name} {func_arguments} {{

{function_body}

}}
"""

sol_struct = """
struct {struct_name} {{

{struct_body}

}}
"""

sol_main_frame = """
contract {contract_name} {{

{contract_structs}


{contract_functions}


}}
"""

class SolidityEngine(object):

    def __init__(self,):
        self.functions = ""
        self.structs = ""

    def buildFunctions(self, 
                       word_array = "", 
                       arg_model = "()",
                       func_bod = ""):
        """
        takes an ordered array and returns
        a large string of functions 
        """
        if len(word_array) < 1: return

        return_funcs = [] 

        #This is dogshit.  Make sure to fix this.  

        for name in word_array:
            try:
                temp_func = sol_func.format(func_name = name, func_arguments = arg_model, function_body = func_bod)
                return_funcs.append(temp_func)

            except:
                pass


        self.functions = "\n\n".join(return_funcs) 



    def buildStructs(self, 
                       word_array = "", 
                       st_name = "Test",
                       st_bod = ""):
        """
        takes an ordered array and returns
        a large string of functions 
        """
       
        if len(word_array) < 1: return

        return_structs = [] 

        #This is also dogshit.  Make sure to fix this.  

        for name in word_array:
            try:
                if name[0].isupper() == False:
                    pass

                else:
                    temp_struct = sol_struct.format(struct_name = name, 
                                            struct_body = st_bod)

                    return_structs.append(temp_struct)

            except:
                pass
        self.structs = "\n\n".join(return_structs) 



    def returnFull(self,name = "TestContract",struct_string = "struct Test{}",func_string = "function Test(){}"):
        return sol_main_frame.format(contract_name = name, 
                              contract_structs = struct_string, 
                              contract_functions= func_string) 



class ChaincodeEngine(object):
    
    def __init__(self):

        pass
