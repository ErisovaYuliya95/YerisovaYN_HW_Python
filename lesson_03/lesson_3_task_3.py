from address import Address
from mail import Mailing

from_address = Address('156958', 'Sakmara', 'Lesnaya', 15, 129)
to_address = Address('954862', 'Orsk', 'Lenina', 154, 89)

mail_to = Mailing(to_address, from_address, 550, str(10002569871110))

print(mail_to)
