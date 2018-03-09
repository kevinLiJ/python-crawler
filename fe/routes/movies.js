var express = require("express");
var router = express.Router();
var operSql = require("./operSql");

/* GET users listing. */
router.get("/", function(req, res, next) {
    operSql("select movie_name,poster_href from movie_info", "", function(
        err,
        result
    ) {
        if (err) {
            res.json({ success: false });
            return;
        }
        res.json({ success: true, result: result });
    });
});

module.exports = router;
