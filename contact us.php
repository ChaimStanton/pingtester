<!DOCTYPE html>
<html>

<?php include 'header.php'; ?>

<body>
    <!-- Start: Contact Form Clean -->
    <div class="contact-clean">
        <form id="contactUsForm" data-bss-recipient="d7baa26bdc82857b5ee3dbf3d0da0425" data-bss-subject="Contact us SpeedTest Website">
            <h2 class="text-center">Contact us</h2>
            <!-- Start: Success Example -->
            <div class="form-group"><input class="form-control" type="text" name="name" placeholder="Name"></div>
            <!-- End: Success Example -->
            <!-- Start: Error Example -->
            <div class="form-group"><input class="form-control is-invalid" type="email" name="email" placeholder="Email">
                <!-- Start: The Error Message --><small class="form-text text-danger">Please enter a correct email address.</small>
                <!-- End: The Error Message -->
            </div>
            <!-- End: Error Example -->
            <div class="form-group"><textarea class="form-control" name="message" placeholder="Message" rows="14"></textarea></div>
            <div class="form-group"><button class="btn btn-primary" type="submit">send </button></div>
        </form>
    </div>
    <!-- End: Contact Form Clean -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>
    <script src="assets/js/smart-forms.min.js"></script>
</body>

<?php include 'footer.php'; ?>

</html>