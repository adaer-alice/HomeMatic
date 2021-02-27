from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class HomeMatic(AliceSkill):
	"""
	Author: adaer-alice
	Description: Skill to use on homematic hardware
	"""


	@IntentHandler('MyIntentName')
	def testIntent(self, session: DialogSession, **_kwargs):
		pass


	@IntentHandler('MySecondIntentName')
	def secondTestIntent(self, session: DialogSession, **_kwargs):
		pass