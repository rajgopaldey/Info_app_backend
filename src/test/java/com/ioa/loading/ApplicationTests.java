import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
@Disabled("Skipping test for CI pipeline")
class InfoAppBackendApplicationTests {

    @Test
    void contextLoads() {
    }
}