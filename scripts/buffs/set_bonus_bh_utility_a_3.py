import sys

def setup(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'expertise_cooldown_line_bh_flawless_strike', 30)
	return	

def removeBuff(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'expertise_cooldown_line_bh_flawless_strike', 30)
	return
	