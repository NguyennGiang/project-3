class FormatService:

    @staticmethod
    def phone_to_canonical_format(phone_number: str) -> str:
        if not phone_number:
            return ""
        phone_number = phone_number.replace(" ", "")
        phone_number = phone_number.strip()
        prefix = phone_number[:4]
        if prefix == "+840":
            return f"+84{phone_number[4:]}"
        return f"+84{phone_number[1:]}" if phone_number.startswith("0") else phone_number