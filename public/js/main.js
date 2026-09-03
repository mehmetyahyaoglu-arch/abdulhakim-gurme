document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('bayilikForm');
    const formStatus = document.getElementById('formStatus');
    const mobileToggle = document.getElementById('mobile-toggle');
    const navLinks = document.querySelector('.nav-links');

    // Mobile menu toggle
    if (mobileToggle) {
        mobileToggle.addEventListener('click', function () {
            if (navLinks.style.display === 'flex') {
                navLinks.style.display = 'none';
            } else {
                navLinks.style.display = 'flex';
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '80px';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.background = '#0A0C10';
                navLinks.style.padding = '20px';
                navLinks.style.borderBottom = '1px solid #D4AF37';
            }
        });
    }

    // Form Submission
    if (form) {
        form.addEventListener('submit', async function (e) {
            e.preventDefault();

            formStatus.className = 'form-status';
            formStatus.style.display = 'none';
            
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Gönderiliyor...';

            const formData = {
                ad_soyad: document.getElementById('ad_soyad').value.trim(),
                telefon: document.getElementById('telefon').value.trim(),
                sehir: document.getElementById('sehir').value.trim(),
                ilce: document.getElementById('ilce').value.trim(),
                butce: document.getElementById('butce').value,
                mesaj: document.getElementById('mesaj').value.trim()
            };

            try {
                const response = await fetch('/api/bayilik-basvuru', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                const result = await response.json();

                if (response.ok && result.success) {
                    formStatus.textContent = result.message || 'Başvurunuz başarıyla alındı!';
                    formStatus.classList.add('success');
                    form.reset();
                } else {
                    formStatus.textContent = result.detail || 'Bir hata oluştu. Lütfen tekrar deneyiniz.';
                    formStatus.classList.add('error');
                }
            } catch (err) {
                console.error('Form gönderme hatası:', err);
                formStatus.textContent = 'Bağlantı hatası oluştu. Lütfen internet bağlantınızı kontrol edip tekrar deneyiniz.';
                formStatus.classList.add('error');
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            }
        });
    }
});
