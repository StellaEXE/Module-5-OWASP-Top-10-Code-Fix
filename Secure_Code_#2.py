// Using Argon2 (via a library like Password4j) or BCrypt
import org.mindrot.jbcrypt.BCrypt;

public String hashPassword(String password) {
    // BCrypt automatically handles salting and is computationally expensive
    return BCrypt.hashpw(password, BCrypt.gensalt(12));
}

public boolean checkPassword(String password, String hashed) {
    return BCrypt.checkpw(password, hashed);
}
