from opshin.prelude import *
from opshin.ledger.interval import *


@dataclass
class PublishingParams(PlutusData):

    publisher: PubKeyHash
    initiator: PubKeyHash
    rngfid: bytes
    seedtxid: bytes
    rngoutput: bytes




@dataclass
class RefundRedeemer(PlutusData):
    pass


def validator(
    datum: PublishingParams, redeemer: RefundRedeemer, context: ScriptContext
) -> None:
    assert datum.publisher in context.tx_info.signatories, "Publisher Sign Missing"