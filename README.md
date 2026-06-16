### Termux / Kali / Ubuntu / Mac OS:


*VBV (Verified by Visa) කියන්නේ payment gateway එකක තියෙන security layer එකක්. සාමාන්‍ය card generator එකකින් හදන card එකක් මේකෙන් අහු වෙනවා.*

ඇත්තම VBV card එකක් "generate" කරන්න බැහැ, මොකද ඒක බැංකුවක server එකක validate වෙන්න ඕනේ. හැබැයි, hackers ලා කරන්නේ BIN (Bank Identification Number) පාවිච්චි කරලා, payment gateways වල "loopholes" හොයන එක සහ CC Checker එකක් මගින් active cards filter කරන එක.මේකෙන් BIN එකක් පාවිච්චි කරලා cards generate කරන්නත්, ඒවා validate කරන්න (Checking) attempt කරන්නත් පුළුවන්.

## The BIN Strategy: 

* හැම බැංකුවකටම වෙනම BIN එකක් තියෙනවා. ඔයාට "Credit" හෝ "Platinum" cards ඕනෙ නම්, අන්තර්ජාලයෙන් "Latest Live BINs" හොයාගනින්. BIN එක හරියටම තියෙනවා නම් card එක "Live" වෙන්න තියෙන chance එක වැඩියි.

## Avoiding Gateways (VBV Bypass): 

* VBV bypass කරන්න නම් ඔයාට ඕනේ "Payment Gateways" (උදා: Stripe, Square, Braintree) වල loopholes තියෙන "Checker" එකක්. ගොඩක් වෙලාවට hackers ලා කරන්නේ "API Manipulation" හරහා payment request එක modify කරන එක.

## Proxy/VPN: 

* මේ වැඩේ කරනකොට අනිවාර්යයෙන්ම Residential Proxies පාවිච්චි කරන්න. නැත්නම් payment gateway එකෙන් ඔයාගේ IP එක block කරනවා. (Datacenter proxies පාවිච්චි කරන්න එපා).

  
```bash
pip install requests colorama
git clone https://github.com/LK-HACKERS/CARD-VBV.git
cd CARD-VBV
python run.py
```  
