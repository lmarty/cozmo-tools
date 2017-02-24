from cozmo_fsm import *

class Junk(StateNode):
    def setup(self):
        """
            startnode: StateNode()
            startnode =TM('1')=> do_null
            startnode =TM('2')=> do_time
            startnode =TM('3')=> do_comp
    
            do_null: Say("Full steam ahead") =N=> Forward(20) =C=> startnode
    
            do_time: Say("Full steam ahead") =T(2)=> Forward(20) =C=> startnode
    
            do_comp: Say("Full steam ahead") =C=> Forward(20) =C=> startnode
        """
        
        # Code generated by genfsm on Thu Feb 16 23:51:48 2017:
        
        startnode = StateNode() .set_name("startnode") .set_parent(self)
        do_null = Say("Full steam ahead") .set_name("do_null") .set_parent(self)
        forward1 = Forward(20) .set_name("forward1") .set_parent(self)
        do_time = Say("Full steam ahead") .set_name("do_time") .set_parent(self)
        forward2 = Forward(20) .set_name("forward2") .set_parent(self)
        do_comp = Say("Full steam ahead") .set_name("do_comp") .set_parent(self)
        forward3 = Forward(20) .set_name("forward3") .set_parent(self)
        
        textmsgtrans1 = TextMsgTrans('1') .set_name("textmsgtrans1")
        textmsgtrans1 .add_sources(startnode) .add_destinations(do_null)
        
        textmsgtrans2 = TextMsgTrans('2') .set_name("textmsgtrans2")
        textmsgtrans2 .add_sources(startnode) .add_destinations(do_time)
        
        textmsgtrans3 = TextMsgTrans('3') .set_name("textmsgtrans3")
        textmsgtrans3 .add_sources(startnode) .add_destinations(do_comp)
        
        nulltrans1 = NullTrans() .set_name("nulltrans1")
        nulltrans1 .add_sources(do_null) .add_destinations(forward1)
        
        completiontrans1 = CompletionTrans() .set_name("completiontrans1")
        completiontrans1 .add_sources(forward1) .add_destinations(startnode)
        
        timertrans1 = TimerTrans(2) .set_name("timertrans1")
        timertrans1 .add_sources(do_time) .add_destinations(forward2)
        
        completiontrans2 = CompletionTrans() .set_name("completiontrans2")
        completiontrans2 .add_sources(forward2) .add_destinations(startnode)
        
        completiontrans3 = CompletionTrans() .set_name("completiontrans3")
        completiontrans3 .add_sources(do_comp) .add_destinations(forward3)
        
        completiontrans4 = CompletionTrans() .set_name("completiontrans4")
        completiontrans4 .add_sources(forward3) .add_destinations(startnode)
        
        return self
