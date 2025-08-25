public class VigenereCipher {

    public static String generateKey(String text, String key) {
        StringBuilder keyBuilder = new StringBuilder(key);
        while (keyBuilder.length() < text.length()) {
            keyBuilder.append(key);
        }
        return keyBuilder.substring(0, text.length()).toUpperCase();
    }

    public static String encrypt(String plaintext, String key) {
        StringBuilder result = new StringBuilder();
        String generatedKey = generateKey(plaintext, key);

        for (int i = 0; i < plaintext.length(); i++) {
            char plainChar = plaintext.charAt(i);
            if (Character.isLetter(plainChar)) {
                char base = Character.isUpperCase(plainChar) ? 'A' : 'a';
                int p = plainChar - base;
                int k = generatedKey.charAt(i) - 'A';
                char encryptedChar = (char) ((p + k) % 26 + base);
                result.append(encryptedChar);
            } else {
                result.append(plainChar);
            }
        }
        return result.toString();
    }

    public static String decrypt(String ciphertext, String key) {
        StringBuilder result = new StringBuilder();
        String generatedKey = generateKey(ciphertext, key);

        for (int i = 0; i < ciphertext.length(); i++) {
            char cipherChar = ciphertext.charAt(i);
            if (Character.isLetter(cipherChar)) {
                char base = Character.isUpperCase(cipherChar) ? 'A' : 'a';
                int c = cipherChar - base;
                int k = generatedKey.charAt(i) - 'A';
                char decryptedChar = (char) ((c - k + 26) % 26 + base);
                result.append(decryptedChar);
            } else {
                result.append(cipherChar);
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        String plaintext = "Hello, World!";
        String key = "KEY";

        String encrypted = encrypt(plaintext, key);
        System.out.println("Encrypted text: " + encrypted);

        String decrypted = decrypt(encrypted, key);
        System.out.println("Decrypted text: " + decrypted);
    }
}
