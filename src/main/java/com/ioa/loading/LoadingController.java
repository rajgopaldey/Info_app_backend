package com.ioa.loading;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LoadingController {

    @GetMapping("/")
    public String home() {
        return "Welcome to Dey Info Backend";
    }

    @GetMapping("/health")
    public String health() {
        return "UP";
    }
}