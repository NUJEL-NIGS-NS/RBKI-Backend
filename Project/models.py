from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Project(models.Model):
    pro_name = models.CharField(_("Project Name"), max_length=255, blank=False)
    district = models.CharField(_("District"), max_length=255, blank=False)
    lac = models.CharField(
        _("Legistative assembly council"), max_length=255, blank=True
    )
    local_bdy = models.CharField(_("Local Body"), max_length=50, blank=True)
    stage = models.CharField(
        _("completed/under construction"), max_length=255, blank=True
    )
    as_no = models.CharField(
        _("administrative sanction no"), max_length=255, blank=True
    )
    as_date = models.DateField(_("administrative sanction date"), blank=True)
    as_amt = models.DecimalField(
        _("administrative sanction amount"), max_digits=10, decimal_places=4, blank=True
    )
    ts_no = models.CharField(_("technical sanction no]"), max_length=255, blank=True)
    ts_date = models.DateField(_("technical sanction date"), blank=True)
    ts_amt = models.DecimalField(
        _("technical sanction amount"), max_digits=10, decimal_places=4, blank=True
    )
    reas_no = models.CharField(
        _("revised administrative sanction no"), max_length=255, blank=True
    )
    reas_date = models.DateField(
        _("revised administrative sanction Date"),
        auto_now=False,
        auto_now_add=False,
        blank=True,
    )
    reas_amt = models.DecimalField(
        _("revised administrative sanction Amount"),
        max_digits=8,
        decimal_places=4,
        blank=True,
    )
    s_date = models.DateField(_("Starting Date"), blank=True)
    pro_cat = models.CharField(_("Project Category"), max_length=255, blank=True)
    length_km = models.DecimalField(
        _("length"), max_digits=10, decimal_places=4, blank=True
    )
    lat_tude = models.DecimalField(
        _("lattitude"), max_digits=10, decimal_places=4, blank=True
    )
    log_tude = models.DecimalField(
        _("logitude"), max_digits=10, decimal_places=4, blank=True
    )
    status = models.CharField(_("current progress"), max_length=255, blank=True)
    piu = models.CharField(_("PIU"), max_length=255, blank=True)
    c_name = models.CharField(_("contractor Name"), max_length=255, blank=True)
    c_phone = models.BigIntegerField(_("contractor phone"), blank=True)
    c_email = models.EmailField(_("contractor email"), max_length=254, blank=True)
    c_pan = models.CharField(_("contractor_PAN"), max_length=50, blank=True)
    tender_no = models.CharField(_("Tender Number"), max_length=255, blank=True)
    tender_data = models.DateField(_("Tender Date"), blank=True)
    tender_amt = models.DecimalField(
        _("Tender Amount"), max_digits=10, decimal_places=4, blank=True
    )
    agr_no = models.CharField(_("agreement no"), max_length=50, blank=True)
    agr_date = models.DateField(
        _("agreement date"), auto_now=False, auto_now_add=False, blank=True
    )
    arg_amt = models.DecimalField(
        _("agreement amount"), max_digits=10, decimal_places=4, blank=True
    )
    hand_to_date = models.DateField(
        _("handover date]"), auto_now=False, auto_now_add=False, blank=True
    )
    period = models.CharField(_("period of completion"), max_length=50, blank=True)
    completion_date = models.DateField(
        _("Complition Date"), auto_now=False, auto_now_add=False, blank=True
    )
    utility = models.CharField(
        _("utility shifting&its amount"), max_length=50, blank=True
    )
    mait_charge = models.DecimalField(
        _("maintenance charge"), max_digits=10, decimal_places=4, blank=True
    )
    total_exp = models.DecimalField(
        _("Total Expenditure"), max_digits=10, decimal_places=4, blank=True
    )
    fin_pro = models.IntegerField(_("financial Progress"), blank=True)
    phy_pro = models.IntegerField(_("Physical Progress"), blank=True)
    updated_by = models.CharField(_("Updated By"), max_length=50, blank=True)
    last_upd = models.DateTimeField(_("Last Update"), auto_now=True, auto_now_add=False)


class Project_file(models.Model):
    pro_name = models.ForeignKey(
        Project, verbose_name=_("Project Name"), on_delete=models.CASCADE
    )
    doc = models.FileField(_("Document"), upload_to="Docs/", max_length=100, blank=True)


class Project_image(models.Model):
    pro_name = models.ForeignKey(
        Project, verbose_name=_("Project Name"), on_delete=models.CASCADE
    )
    image = models.ImageField(
        _("image"),
        upload_to="Images",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
    )


class Project_Video(models.Model):
    pro_name = models.ForeignKey(
        Project, verbose_name=_("Project Name"), on_delete=models.CASCADE
    )
    video = models.FileField(
        _("video"), upload_to="Videos/", max_length=100, blank=True
    )

class Project_constants(models.Model):
    as_id = models.IntegerField(_("as_id"))
    as_awarded = models.DecimalField(_("as_awarded"), max_digits=10, decimal_places=4)
    alc_fr_rki = models.DecimalField(_("allocation from rki"), max_digits=7, decimal_places=2)


class Update_project(models.Model):
        pro_name = models.CharField(_("Project Name"), max_length=255, blank=False)
        district = models.CharField(_("District"), max_length=255, blank=False)
        lac = models.CharField(
            _("Legistative assembly council"), max_length=255, blank=True
        )
        local_bdy = models.CharField(_("Local Body"), max_length=50, blank=True)
        stage = models.CharField(
            _("completed/under construction"), max_length=255, blank=True
        )
        as_no = models.CharField(
            _("administrative sanction no"), max_length=255, blank=True
        )
        as_date = models.DateField(_("administrative sanction date"), blank=True)
        as_amt = models.DecimalField(
            _("administrative sanction amount"), max_digits=10, decimal_places=4, blank=True
        )
        ts_no = models.CharField(_("technical sanction no]"), max_length=255, blank=True)
        ts_date = models.DateField(_("technical sanction date"), blank=True)
        ts_amt = models.DecimalField(
            _("technical sanction amount"), max_digits=10, decimal_places=4, blank=True
        )
        reas_no = models.CharField(
            _("revised administrative sanction no"), max_length=255, blank=True
        )
        reas_date = models.DateField(
            _("revised administrative sanction Date"),
            auto_now=False,
            auto_now_add=False,
            blank=True,
        )
        reas_amt = models.DecimalField(
            _("revised administrative sanction Amount"),
            max_digits=8,
            decimal_places=4,
            blank=True,
        )
        s_date = models.DateField(_("Starting Date"), blank=True)
        pro_cat = models.CharField(_("Project Category"), max_length=255, blank=True)
        length_km = models.DecimalField(
            _("length"), max_digits=10, decimal_places=4, blank=True
        )
        lat_tude = models.DecimalField(
            _("lattitude"), max_digits=10, decimal_places=4, blank=True
        )
        log_tude = models.DecimalField(
            _("logitude"), max_digits=10, decimal_places=4, blank=True
        )
        status = models.CharField(_("current progress"), max_length=255, blank=True)
        piu = models.CharField(_("PIU"), max_length=255, blank=True)
        c_name = models.CharField(_("contractor Name"), max_length=255, blank=True)
        c_phone = models.BigIntegerField(_("contractor phone"), blank=True)
        c_email = models.EmailField(_("contractor email"), max_length=254, blank=True)
        c_pan = models.CharField(_("contractor_PAN"), max_length=50, blank=True)
        tender_no = models.CharField(_("Tender Number"), max_length=255, blank=True)
        tender_data = models.DateField(_("Tender Date"), blank=True)
        tender_amt = models.DecimalField(
            _("Tender Amount"), max_digits=10, decimal_places=4, blank=True
        )
        agr_no = models.CharField(_("agreement no"), max_length=50, blank=True)
        agr_date = models.DateField(
            _("agreement date"), auto_now=False, auto_now_add=False, blank=True
        )
        arg_amt = models.DecimalField(
            _("agreement amount"), max_digits=10, decimal_places=4, blank=True
        )
        hand_to_date = models.DateField(
            _("handover date]"), auto_now=False, auto_now_add=False, blank=True
        )
        period = models.CharField(_("period of completion"), max_length=50, blank=True)
        completion_date = models.DateField(
            _("Complition Date"), auto_now=False, auto_now_add=False, blank=True
        )
        utility = models.CharField(
            _("utility shifting&its amount"), max_length=50, blank=True
        )
        mait_charge = models.DecimalField(
            _("maintenance charge"), max_digits=10, decimal_places=4, blank=True
        )
        total_exp = models.DecimalField(
            _("Total Expenditure"), max_digits=10, decimal_places=4, blank=True
        )
        fin_pro = models.IntegerField(_("financial Progress"), blank=True)
        phy_pro = models.IntegerField(_("Physical Progress"), blank=True)
        updated_by = models.CharField(_("Updated By"), max_length=50, blank=True)
        last_upd = models.DateTimeField(_("Last Update"), auto_now=True, auto_now_add=False)   


class Update_cache_table(models.Model):
     pro_id =models.IntegerField(_("project id"),unique=True)
     upd_id = models.IntegerField(_("updation_id"),unique=True)       