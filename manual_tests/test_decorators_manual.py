

SWITCH = 'Answer'
# SWITCH = 'Question'
# __Q: t160422 t160710 tp3 t170304 tp4 t190213 t241216 tp5 t420624 tp6 rm3.0
print('\n\n\n\n--- --- --- QUESTION: Make it so the input and output of this fcn are logged (showing msg box)! --- --- ---')
if SWITCH == 'Question':
    def logged_fcn(a, b):
        return a*b

if SWITCH == 'Answer': # __A:
    import decorators
    @decorators.log_fcn_in_out(1)
    def logged_fcn(a, b, c=5, d=9, e=4):
        return a*b

def tst_log_fcn_in_out():
    logged_fcn(3, b=6)

tst_log_fcn_in_out()



