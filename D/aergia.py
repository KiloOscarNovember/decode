from fn import *

#http://aergia.ts-morpheus.com/

if False:
    #Challenge #001, very easy, 1 layer
    cipher1 = '''Rirel bapr va n juvyr V'yy hcqngr gur fvgr jvgu fznyy punyyratrf. Gurve qvssvphygl pna enatr sebz irel rnfl gb irel uneq naq gurl pna pbagnva zrqvn be bgure vasbezngvba gung unf gb or qrpbqrq. Vs lbh unir fhpprffshyyl qrpbqrq n punyyratr, lbh'yy qvfpbire n cnffcuenfr gung lbh unir gb frag gb zr. Nybat jvgu lbhe ntrag anzr naq snpgvba, frag gur cnffcuenfr gb @CvCevzr ba Gryrtenz. Jub xabjf, znlor gurl'yy or fbzr cnffpbqrf jnvgvat...? CNFFCUENFR: "Pbtvgb, retb fhz."'''
    
    print(rot(cipher1,13))

if False:
    #Challenge #002, easy, 2 layers
    cipher2 = '061 062 064 040 061 065 060 040 061 064 065 040 061 066 062 040 061 064 065 040 060 064 060 040 061 065 061 040 061 066 063 040 060 064 060 040 061 064 061 040 060 064 060 040 061 066 060 040 061 065 064 040 061 064 061 040 061 064 063 040 061 064 065 040 060 065 066 040 060 064 060 040 061 061 064 040 061 065 061 040 061 065 063 040 061 064 065 040 060 064 060 040 061 065 066 040 061 065 067 040 060 064 060 040 061 066 060 040 061 065 064 040 061 064 061 040 061 064 063 040 061 064 065 040 060 064 060 040 061 065 067 040 061 065 066 040 060 064 060 040 061 060 065 040 061 064 061 040 061 066 062 040 061 066 064 040 061 065 060 040 060 065 066 040 060 064 060 040 061 060 061 040 060 064 060 040 061 065 064 040 061 064 061 040 061 065 066 040 061 064 064 040 060 064 060 040 061 064 066 040 061 066 065 040 061 065 064 040 061 065 064 040 060 064 060 040 061 065 067 040 061 064 066 040 060 064 060 040 061 066 067 040 061 065 067 040 061 065 066 040 061 064 064 040 061 064 065 040 061 066 062 040 060 065 064 040 060 064 060 040 061 065 065 040 061 067 061 040 061 066 063 040 061 066 064 040 061 064 065 040 061 066 062 040 061 067 061 040 060 065 064 040 060 064 060 040 061 064 061 040 061 065 066 040 061 064 064 040 060 064 060 040 061 064 064 040 061 064 061 040 061 065 066 040 061 064 067 040 061 064 065 040 061 066 062 040 060 064 061 040 060 064 060 040 061 062 063 040 061 065 067 040 061 065 065 040 061 064 065 040 060 064 060 040 061 066 063 040 061 064 061 040 061 067 061 040 060 064 060 040 061 066 064 040 061 065 067 040 060 064 060 040 061 066 063 040 061 066 065 040 061 066 062 040 061 066 066 040 061 065 061 040 061 066 066 040 061 064 065 040 060 064 060 040 061 065 061 040 061 066 064 040 060 067 062 040 060 064 060 040 061 063 061 040 061 065 067 040 061 066 065 040 060 064 060 040 061 065 066 040 061 064 065 040 061 064 065 040 061 064 064 040 060 064 060 040 061 066 064 040 061 065 067 040 060 064 060 040 061 064 062 040 061 064 065 040 060 064 060 040 061 064 061 040 061 066 063 040 060 064 060 040 061 065 065 040 061 064 061 040 061 064 064 040 060 064 060 040 061 064 061 040 061 066 063 040 060 064 060 040 061 064 061 040 060 064 060 040 061 065 060 040 061 064 061 040 061 066 064 040 061 066 064 040 061 064 065 040 061 066 062 040 060 065 066 040 060 064 060 040 061 062 060 040 061 060 061 040 061 062 063 040 061 062 063 040 061 062 060 040 061 061 060 040 061 062 062 040 061 060 061 040 061 062 063 040 061 060 065 040 060 067 062 040 060 064 060 040 061 061 065 040 061 064 061 040 061 064 064 040 060 064 060 040 061 061 060 040 061 064 061 040 061 066 064 040 061 066 064 040 061 064 065 040 061 066 062'
    
    a= cipher2.split(' ')
    b= ''.join([chr(int(x,8)) for x in a])
    c= b.split(' ')
    d= ''.join([chr(int(x,8)) for x in c])
    print(d)
    
if False:
    #Challenge #003, easy, 2 layers
    cipher3='''guzI :VHZISKHHZK .dlm lt oo'R !pxfo wzY/wllT .mlmzx try vsg ul vizdz boml vY .gr vpzn oo'flb ,biild g'mlW .hgmzhzvk dlm vgzu iflb lg flb vezvo oord R .flb sxgzx oord bvsg viluvy dlm lT !wllT ?gr glt ...vivsG !gr ivynvnvi ghfn flB .hovmmfg vsg stflisg flb vwrft lg kzn z hr vivs :flb kovs oord R ,biild g'mlw gfY .bgvuzh lg guzi vsg vwrft ghfn flB'''
    
    a=rev(cipher3)
    b=atbash(a)
    print(b)
    
if False:
    #Challenge #004, hard, 4 layers
    cipher4='59 57 56 79 5a 32 6c 68 4c 6e 52 7a 4c 57 31 76 63 6e 42 6f 5a 58 56 7a 4c 6d 4e 76 62 53 39 6a 61 47 46 73 62 47 56 75 5a 32 56 7a 4c 7a 41 77 4e 43 35 6d 61 57 78 6c'
    a=cipher4.split(' ')
    b=''.join([chr(int(x,16)) for x in a])
    import base64
    c=base64.b64decode(b)
    print(c)

    # https://academo.org/demos/spectrum-analyzer/
    # Passphrase: Japan
    
if False:
    #Challenge #005, hard, 3 layers
    cipher5='PV1cWEw9dSdvLTlRIWFTOU5OcmxAcj1WTz4kK2dPOVBtT0pAVCw6JUA3TmUuQFJqSUE9dSctKTlSOSFLOi9hL3A+JCFGcEBXIyhlPT5EVVNAcjYiKEA3WDo8QFIzLj8='
    import base64
    a=base64.b64decode(cipher5)
    b=base64.a85decode(a)
    c=base64.b64decode(b)
    print(c)
    #https://youtu.be/y1Xo_gt3cno
    #PASSPHRASE MEMENTO
    
if False:
    #Challenge #006, normal, 3 layers
    cipher6='==gdupHVgY3cHBiOWhkWJN1SIhkWLpgLnhGbvByZoZWcgw2ckBCcsx2TKAiLv9mdEpAIu4iLKIiLoZHaox2bgUHbgkmd55mZtBidzdGI2hme2lGetJHIilndpZ3cnBydtpHI25meUBidzdEI1xGI2lmekpHI292asZ3agUHbgkmd55mZtBidzdGI2hme2lGetJHIsdGI3Z3as9mdlZ3dg0md2lHI2VmezBCa4J3Z4p3Rg4iduJ3ZgY3cnBybvpHInJHI01mcip3brBidppHIsYnb6RHI2N3ZgUHbgYXa6RmegYHasN3Zg82b6BSasBCL39WasRGI29GbzRGI2N3ZgwidupHVgY3cHBSdsBSbsJ3Z6JXa6VGI2N3Zg0GbgQXbydXb2tmdXBiL25meUBidzdEI1xGIo1GbyhWa2VGInhGbuBSbyRGIsdGI29WeyhGastmbyBCayByZSBiLolmZ4hHbgcmcgYnbydGIzhne2Byd2hXbmxWbtpHI2lHInhmZuByc4J3ckBCLohGbvBieggmdnZ2ZydGatxGegYnb6RFI2N3RgcmZslnegQXbyBXbyN3Rg4SdvZHanJHI25meUBidzdEInZGb5pHI01mcw1mczdGI3JHblpHIsdGIoJHI2VmcnhndxlHbgY3cnBidpZ3ckBidupHdg8men1mduBieggmcgYnb6RFI2N3RiAiO6J3d2tmcwJHRgY3ZsZmagw2Rg4iI25meUBidzdkIgw2ZgYGbiBid4Z2dsl2ZtJHI25GInZ3Tg4iduBSbyByZoZXa2dWbyByZox2bgYXZ6NHI3diZsJGInNHdmx2cnBiUgESbypHd6ByZ2ZnbgYHR'
    
    a= rev(cipher6)
    import base64
    b=base64.b64decode(a).decode('utf-8')
    c=atbash(b)
    print(c)
    